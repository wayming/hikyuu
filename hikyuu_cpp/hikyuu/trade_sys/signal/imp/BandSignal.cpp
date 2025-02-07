/*
 * BandSignal.cpp
 *
 *   Created on: 2023年09月23日
 *       Author: yangrq1018
 */
#include "../../../indicator/crt/KDATA.h"
#include "BandSignal.h"

#if HKU_SUPPORT_SERIALIZATION
BOOST_CLASS_EXPORT(hku::BandSignal)
#endif

namespace hku {

BandSignal::BandSignal() : SignalBase("SG_Band") {}

BandSignal::BandSignal(const Indicator& ind, price_t lower, price_t upper)
: SignalBase("SG_Band"), m_ind(ind), m_lower(lower), m_upper(upper) {
    HKU_ERROR_IF(lower > upper, "BandSignal: lower track is greater than upper track");
}

BandSignal::~BandSignal() {}

SignalPtr BandSignal::_clone() {
    BandSignal* p = new BandSignal();
    p->m_upper = m_upper;
    p->m_lower = m_lower;
    p->m_ind = m_ind.clone();
    return SignalPtr(p);
}

void BandSignal::_calculate() {
    Indicator ind = m_ind(m_kdata);
    size_t discard = ind.discard();
    size_t total = ind.size();

    for (size_t i = discard; i < total; ++i) {
        if (ind[i] > m_upper) {
            _addBuySignal(m_kdata[i].datetime);
        } else if (ind[i] < m_lower) {
            _addSellSignal(m_kdata[i].datetime);
        }
    }
}

SignalPtr HKU_API SG_Band(const Indicator& sig, price_t lower, price_t upper) {
    return SignalPtr(new BandSignal(sig, lower, upper));
}

}  // namespace hku